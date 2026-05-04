# ZDI-10-136: Novell Teaming ajaxUploadImageFile Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-136
- **ZDI-CAN:** ZDI-CAN-777
- **Date:** 2010-07-21
- **CVE:** CVE-2010-2773
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Access Manager
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-136/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Teaming. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Tomcat server installed by default with Teaming. The server exposes an AJAX request handler which allows a remote user to upload an image via the upload_image_file operation. By crafting a specially formatted filename an attacker can bypass a name-mangling mechanism and traverse outside the intended temporary directory. By uploading a malicious JSP document to the web directory, an attacker can abuse this functionality to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=gz4IRLKEfDo~

## Disclosure Timeline

- 2010-07-19 - Vulnerability reported to vendor
- 2010-07-21 - Coordinated public release of advisory
