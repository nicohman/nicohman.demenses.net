(defun export ()
  (require 'org)
  (setq org-publish-use-timestamps-flag nil)
  (setq org-publish-project-alist '(("nicohman-org" :base-directory "~/nicohman.demenses.net/org"
                                     :base-extension "org"
                                     :publishing-directory "~/nicohman.demenses.net/export"
                                     :publishing-function org-html-publish-to-html
                                     :headline-levels 10
                                     :with-author nil
                                     :html-validation-link nil
                                     :with-timestamps nil
                                     :html-postamble nil
                                     :html-toplevel-hlevel 3
                                     :html-head "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"fonts.css\">"
                                     :html-link-home "index.html"
                                     :section-numbers nil)
                                    ("nicohman-static" :base-directory "~/nicohman.demenses.net/static"
                                     :base-extension any
                                     :publishing-directory "~/nicohman.demenses.net/export"
                                     :publishing-function org-publish-attachment
                                     :recursive t)
                                    ("nicohman" :components ("nicohman-org" "nicohman-static"))))
  (org-publish-project "nicohman"))
