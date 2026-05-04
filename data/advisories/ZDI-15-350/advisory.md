# ZDI-15-350: Belkin N300 Dual-Band Wi-Fi Range Extender formWlanSetupWPS wps_enrolee_pin Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-350
- **ZDI-CAN:** ZDI-CAN-2640
- **Date:** 2015-07-20
- **CVE:** CVE-2015-5536
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Belkin
- **Affected Products:** N300 Dual-Band Wi-Fi Range Extender
- **Credit:** Elvis Collado of HP DVLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-350/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Belkin N300 Dual-Band Wi-Fi Range Extender. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of formWlanSetupWPS requests. It is possible to inject arbitrary operating system commands when the application is handling the wps_enrolee_pin parameter. A remote attacker can leverage this vulnerability to execute remote code under the context of the root user.

## Additional Details

Belkin has issued an update to correct this vulnerability. More details can be found at: http://www.belkin.com/us/support-article?articleNum=4975

## Disclosure Timeline

- 2014-11-26 - Vulnerability reported to vendor
- 2015-07-20 - Coordinated public release of advisory
