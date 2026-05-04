# ZDI-13-049: Novell ZENworks Control Center File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-049
- **ZDI-CAN:** ZDI-CAN-1527
- **Date:** 2013-03-22
- **CVE:** CVE-2013-1080
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** James Burton Insomnia Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-049/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENworks. Authentication is not required to exploit this vulnerability. The specific issues exists within ZENworks Control Center which listens on tcp/443 by default. Insufficient authentication checking on /zenworks/jsp/index.jsp allows a remote attacker to upload files to the webserver. By combining this with a directory traversal vulnerability, an attacker can exploit this condition to gain remote code execution as SYSTEM.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7011812

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2013-03-22 - Coordinated public release of advisory
