# ZDI-15-437: Moxa SoftCMS VLCControl setUserInfoData strIP Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-437
- **ZDI-CAN:** ZDI-CAN-2999
- **Date:** 2015-09-08
- **CVE:** CVE-2015-6457
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Moxa
- **Affected Products:** SoftCMS
- **Credit:** Fritz Sands - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-437/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Moxa SoftCMS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of the strIP parameter of the setUserInfoData method of the VLCPlugin control. The IP address string is copied to a fixed-length heap buffer without a length validation. An attacker can leverage this vulnerability to gain code execution under the context of the process.

## Additional Details

Moxa has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-239-01

## Disclosure Timeline

- 2015-06-11 - Vulnerability reported to vendor
- 2015-09-08 - Coordinated public release of advisory
