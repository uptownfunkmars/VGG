import tensorflow as tf

# test tensorboard


# x = tf.placeholder(tf.bool)
# output = tf.cond(x, lambda : 1, lambda : 2)
#
# with tf.Session() as sess:
#     ans = sess.run(output, {x:True})
#     print(ans)

# 定义静态图
# x = tf.placeholder(tf.float32, [3], name="input")
# weight = tf.Variable([10, 11, 12], dtype=tf.float32)
# y = tf.multiply(x, weight)

# 下述语句保存的即为.pb文件
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     ans = sess.run(y, {x: [1, 2, 3]})
#     print(ans)
#
#     save_path = "saved_path"
#     builder = tf.saved_model.builder.SavedModelBuilder(save_path)
#
#     x_tensorInfo = tf.saved_model.utils.build_tensor_info(x)
#     weight_tensorInfo = tf.saved_model.utils.build_tensor_info(weight)
#     y_tensorInfo = tf.saved_model.utils.build_tensor_info(y)
#
#     signatureDef = tf.saved_model.signature_def_utils.build_signature_def(
#         inputs={'input_1': x_tensorInfo, 'input_2': weight_tensorInfo},
#         outputs={'output': y_tensorInfo},
#         method_name='test')
#
#     builder.add_meta_graph_and_variables(sess,
#                                          tags=[tf.saved_model.tag_constants.TRAINING],
#                                          signature_def_map={
#                                              tf.saved_model.signature_constants.CLASSIFY_INPUTS: signatureDef
#                                          })
#
#     builder.save()


# 加载pb文件，重新运行。
# with tf.Session() as sess:
#     path = "saved_path"
#     MetaGraphDef = tf.saved_model.load(sess, tags=[tf.saved_model.tag_constants.TRAINING], export_dir=path)
#
#     signatureDef_d = MetaGraphDef.signature_def
#     signatureDef = signatureDef_d[tf.saved_model.signature_constants.CLASSIFY_INPUTS]
#
#     x_TensorInfo = signatureDef.inputs['input_1']
#     weight_TensorInfo = signatureDef.inputs['input_2']
#     y_TensorInfo = signatureDef.outputs['output']
#
#     x = tf.saved_model.get_tensor_from_tensor_info(x_TensorInfo, sess.graph)
#     weight = tf.saved_model.get_tensor_from_tensor_info(weight_TensorInfo, sess.graph)
#     y = tf.saved_model.get_tensor_from_tensor_info(y_TensorInfo, sess.graph)
#
#     print(sess.run(weight))
#     print(sess.run(y, {x: [3, 2, 1]}))


# a = tf.Variable(tf.random_normal([4, 5, 5, 3], dtype=tf.float32), name="V1")
#
# mean, var = tf.nn.moments(a, [0, 1, 2])
#
#
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(sess.run(a))
#     print(a.get_shape().as_list())
#     print(sess.run(mean))
#     print(sess.run(var))
#
#     print(mean.get_shape().as_list())
#     print(var.get_shape().as_list())

# tf.get_variable()

# def dataGen(num):
#     for i in range(num):
#         yield i, i + 2
#
# dg = dataGen(10)
#
# for x, y in dg:
#     print(x, y)
