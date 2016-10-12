import tensorflow as tf
import pandas as pd
import tempfile

COLUMNS = ["reach","like","comment","share"]
FEATURE_COLUMNS = ["like","comment","share",]
flags = tf.app.flags
FLAGS = flags.FLAGS

flags.DEFINE_string("model_dir", "", "Base directory for output models.")
flags.DEFINE_integer("train_steps", 10000, "Number of training steps.")
#def get_data_from_file():
#    train_file = open("trainData.txt","r")
#    test_file = open("testData.txt","r")
#    return train_file, test_file

#df_train = pd.read_csv()



def build_estimator(model_dir):
    #"""Build an estimator."""
    like = tf.contrib.layers.real_valued_column("like")
    comment = tf.contrib.layers.real_valued_column("comment")
    share = tf.contrib.layers.real_valued_column("share")
    wide_columns =[like,comment,share]

    m = tf.contrib.learn.LinearRegressor(feature_columns=wide_columns,optimizer=tf.train.FtrlOptimizer(learning_rate=0.01,l1_regularization_strength=0.1),model_dir=model_dir)
    return m

def input_fn(df):
    #"""Input builder function."""
    features_cols = {k: tf.constant(df[k].values) for k in FEATURE_COLUMNS}

    #features_cols = dict(feature_cols)
    outcome = tf.constant(df["reach"].values)
    return features_cols,outcome

def train_and_eval():
    #"""Train and evaluate the model."""
    df_train = pd.read_csv(
      tf.gfile.Open("train"),
      names=COLUMNS,
      skipinitialspace=True,
      engine="python")
    df_test = pd.read_csv(
      tf.gfile.Open("test"),
      names=COLUMNS,
      skipinitialspace=True,
      skiprows=1,
      engine="python")
    model_dir = tempfile.mkdtemp() if not FLAGS.model_dir else FLAGS.model_dir
    print("model directory = %s" % model_dir)
    m = build_estimator(model_dir)
    m.fit(input_fn=lambda: input_fn(df_train), steps = FLAGS.train_steps)
    results = m.evaluate(input_fn=lambda: input_fn(df_test),steps=1)
    for key in sorted(results):
        print("%s: %s" % (key, results[key]))

def main(_):
  train_and_eval()


if __name__ == "__main__":
  tf.app.run()