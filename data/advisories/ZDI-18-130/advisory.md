# ZDI-18-130: Dahua Technology IP Camera Predictable Password Algorithm Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-130
- **ZDI-CAN:** ZDI-CAN-4956
- **Date:** 2018-01-19
- **CVE:** CVE-2017-9315
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Dahua Technology
- **Affected Products:** IP Camera
- **Credit:** Kenney Lu Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-130/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Dahua Technology IP Camera. Authentication is not required to exploit this vulnerability. The specific flaw exists within the disaster recovery password functionality. If the device uses its default settings, the password generation algorithm produces a predictable result. An attacker can leverage this vulnerability to gain control of the device under attack.

## Additional Details

Dahua Technology has issued an update to correct this vulnerability. More details can be found at: http://www.dahuasecurity.com/Support/Cybersecurity/annoucementNotice/152

## Disclosure Timeline

- 2017-07-16 - Vulnerability reported to vendor
- 2018-01-19 - Coordinated public release of advisory
