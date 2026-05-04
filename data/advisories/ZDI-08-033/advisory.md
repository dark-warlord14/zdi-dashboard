# ZDI-08-033: Motorola RAZR JPG Processing Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-033
- **ZDI-CAN:** ZDI-CAN-222
- **Date:** 2008-05-27
- **CVE:** CVE-2008-2548
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Motorola
- **Affected Products:** RAZR
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-033/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable Motorola RAZR firmware based cell phones. User interaction is required to exploit this vulnerability in that the target must accept a malicious image sent via MMS. The specific flaw exists in the JPEG thumbprint component of the EXIF parser. A corrupt JPEG received via MMS can cause a memory corruption which can be leveraged to execute arbitrary code on the affected device.

## Additional Details

Together, ZDI and Motorola have identified a potential vulnerability related to viewing malicious, manipulated JPEG files affecting select RAZR-series devices. Although the possibility of this vulnerability occurring is very remote and would only occur in unique circumstances, Motorola proactively corrected it in all new device releases. To ensure that you have the latest software load available for your device, please visit: http://direct.motorola.com/hellomoto/NSS/update_my_software.asp

## Disclosure Timeline

- 2007-07-10 - Vulnerability reported to vendor
- 2008-05-27 - Coordinated public release of advisory
