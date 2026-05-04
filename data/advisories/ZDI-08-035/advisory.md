# ZDI-08-035: CA ETrust Secure Content Manager Gateway FTP PASV Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-035
- **ZDI-CAN:** ZDI-CAN-340
- **Date:** 2008-06-04
- **CVE:** CVE-2008-2541
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** eTrust Secure Content Manager
- **Credit:** Sebastian Apelt (webmaster@buzzworld.org)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-035/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Computer Associates eTrust Secure Content Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists in the HTTP Gateway service icihttp.exe running on port 8080. By specifying a overly long response to a PASV command a stack buffer can be overflowed. Successful exploitation can lead to complete system compromise under the SYSTEM context.

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID=177784

## Disclosure Timeline

- 2008-05-23 - Vulnerability reported to vendor
- 2008-06-04 - Coordinated public release of advisory
