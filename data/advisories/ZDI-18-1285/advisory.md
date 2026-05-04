# ZDI-18-1285: OMRON CX-Supervisor PAG Image Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1285
- **ZDI-CAN:** ZDI-CAN-6419
- **Date:** 2018-10-17
- **CVE:** CVE-2018-17907
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** OMRON
- **Affected Products:** CX-Supervisor
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1285/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of OMRON CX-Supervisor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of image files. A crafted bitmap in a PAG file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

OMRON has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-290-01

## Disclosure Timeline

- 2018-06-28 - Vulnerability reported to vendor
- 2018-10-17 - Coordinated public release of advisory
- 2018-10-17 - Advisory Updated
