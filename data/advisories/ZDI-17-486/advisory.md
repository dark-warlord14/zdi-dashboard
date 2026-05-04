# ZDI-17-486: Adobe Flash BrokerCreateFile Broker Method Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-486
- **ZDI-CAN:** ZDI-CAN-4640
- **Date:** 2017-07-12
- **CVE:** CVE-2017-3080
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-486/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the Enhanced Protected Mode sandbox of vulnerable installations of Adobe Flash Player and disclose file contents. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the BrokerCreateFile method. An attacker can use this component to read the contents of any file that the current user has access to.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb17-21.html

## Disclosure Timeline

- 2017-03-30 - Vulnerability reported to vendor
- 2017-07-12 - Coordinated public release of advisory
