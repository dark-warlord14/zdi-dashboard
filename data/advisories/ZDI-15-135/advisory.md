# ZDI-15-135: IBM Lotus Domino GIF Integer Truncation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-135
- **ZDI-CAN:** ZDI-CAN-2718
- **Date:** 2015-04-15
- **CVE:** CVE-2015-0135
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** bilou
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-135/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Domino. Authentication is not required to exploit this vulnerability. The flaw exists within the nrouter.exe component which handles e-mails dispatched from nsmtp.exe listening on port 25. By specifying malicious dimensions within a GIF, an integer truncation can occur potentially resulting in an undersized buffer being allocated. A remote attacker could exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21701647

## Disclosure Timeline

- 2015-01-27 - Vulnerability reported to vendor
- 2015-04-15 - Coordinated public release of advisory
