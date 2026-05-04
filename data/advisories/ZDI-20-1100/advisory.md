# ZDI-20-1100: Cisco RV340 upload.cgi Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1100
- **ZDI-CAN:** ZDI-CAN-10640
- **Date:** 2020-09-08
- **CVE:** CVE-2020-3451
- **CVSS:** 5.5
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1100/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Cisco RV340 routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of the fileparam parameter provided to the upload.cgi endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the www-data user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-rv-osinj-rce-pwTkPCJv

## Disclosure Timeline

- 2020-05-26 - Vulnerability reported to vendor
- 2020-09-08 - Coordinated public release of advisory
