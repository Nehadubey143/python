# <!doctype html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>Flexbox</title>
#   </head>
#   <!-- clsss:-Indicates the Class of the element (non-unique) -->
#   <!-- id :-indicates the ID of the element (unique in the same context)-->
#   <style>
#     p {
#       width: 80px;
#       height: 80px;
#       color: greenyellow;
#       background-color: blue;
#       border-radius: 20px;
#       font-weight: bold;
#       text-align: center;
#       border: 10px solid red;
#     }
#     /* we can apply css for any class via "." */
#     .main {
#       display: flex;
#       /* Default value. */
#       /* flex-direction: row; */
#       /* flex-direction: row-reverse; */

#       /*Output  Box4 --> box3 --> box2 --> box1 */

#       flex-direction: column;
#       /*Output
#       Box1
#       Box2
#       Box3
#       Box4 */
#       /* flex-direction: column-reverse; */
#       /* Output
#       Box4
#       Box3
#       Box2
#       Box1 */
#       /* justify-content:- justify content work X axis wise ,it will work when flex direction = row */

#       /* justify-content:flex-start ;  */
#       /* Items are placed at the beginning. */
#       /* justify-content: flex-end; */
#       /* Items are placed at the end. */
#       /* justify-content: center; */
#       /* Items are placed in the center. */
#       /* justify-content: space-around; */
#       /* Space is placed around each item. */
#       /* justify-content: space-between; */
#       /* Equal space is placed between the items. */
#       /* justify-content: space-evenly; */
#       /* Equal space is placed between items and at the edges. */
#       /* --------------------------------------------------------------------
#        */
#       gap: 20px;
#     }
#   </style>
#   <body>
#     <!-- FlexBox:-Flexbox(Flexible Box layout) is a CSS layout system used to arrange HTML Element easily in row or columns

#     we can apply display flex on only parent tag 

# Horizontal → Row
# Vertical→ Column
#  -->

#     <div class="main">
#       <p>Box1</p>
#       <p>Box2</p>
#       <p>Box3</p>
#       <p>Box4</p>
#     </div>
#   </body>
# </html>