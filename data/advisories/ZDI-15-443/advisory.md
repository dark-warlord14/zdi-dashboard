# ZDI-15-443: Symantec Web Gateway Arbitrary PHP File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-443
- **ZDI-CAN:** ZDI-CAN-2917
- **Date:** 2015-09-16
- **CVE:** CVE-2015-5691 , CVE-2015-5692
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:M/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** Web Gateway
- **Credit:** Jos Wetzels - LeakFree Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-443/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Web Gateway. Authentication is required to exploit this vulnerability, however it can be bypassed via reflected cross-site scripting. The specific flaw exists within the admin_messages.php file which relies on mimetypes and file extensions to block potentially dangerous file uploads. An attacker can exploit this condition to upload arbitrary files as the apache user. Due to loose sudo restrictions, an attacker can add the setuid attribute and execute arbitrary code under the context of root.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=&suid=20150916_00

## Disclosure Timeline

- 2015-05-06 - Vulnerability reported to vendor
- 2015-09-16 - Coordinated public release of advisory
