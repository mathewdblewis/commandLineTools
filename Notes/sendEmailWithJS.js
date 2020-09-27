var nodemailer = require('nodemailer')

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'theGpsTrackingApp@gmail.com',
    pass: 'alskdjfslkdjflskjSLDKJFSLDKJ(&6987987'
}
})

var mailOptions = {
  from:     'theGpsTrackingApp@gmail.com',
  to:       'mathewdblewis@protonmail.com',
  subject:  'test subj',
  text:     'test body'
}

transporter.sendMail(mailOptions,function(error,info){
  if (error) {
    console.log(error)
  } else {
    console.log('Email sent: ' + info.response)
  }
})


