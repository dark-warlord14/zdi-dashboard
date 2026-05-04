# ZDI-15-193: IBM Lotus Domino BMP Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-193
- **ZDI-CAN:** ZDI-CAN-2717
- **Date:** 2015-05-12
- **CVE:** CVE-2015-1902
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** bilou
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-193/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Domino. Authentication is not required to exploit this vulnerability. The flaw exists within the nrouter.exe component which handles e-mails dispatched from nsmtp.exe listening on port 25. By specifying malicious dimensions within a BMP, an integer overflow can occur potentially resulting in an undersized buffer being allocated. A remote attacker could exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www.ibm.com/support/docview.wss?uid=swg21883245

## Disclosure Timeline

- 2015-02-10 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory
