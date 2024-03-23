resource "aws_alb" "alb" {
  name               = var.name
  internal           = false
  load_balancer_type = "application"

  subnets         = var.subnet_ids
  security_groups = var.security_group_ids

  enable_deletion_protection = true
  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_alb_listener" "listener_http" {
  load_balancer_arn = aws_alb.alb.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "fixed-response"

    fixed_response {
      content_type = "text/plain"
      status_code  = "503"
      message_body = "Request not matched."
    }
  }
}

# resource "aws_alb_listener" "listener_https" {
#   load_balancer_arn = aws_alb.alb.arn
#   port              = "443"
#   protocol          = "HTTPS"
#   certificate_arn   = aws_acm_certificate.dub_washington_edu.arn
#
#   default_action {
#     type             = "fixed-response"
#
#     fixed_response {
#       content_type = "text/plain"
#       status_code  = "503"
#       message_body = "Request not matched."
#     }
#   }
# }
