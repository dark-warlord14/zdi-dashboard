# ZDI-06-051: Mozilla Firefox SVG Processing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-051
- **ZDI-CAN:** ZDI-CAN-126
- **Date:** 2006-12-19
- **CVE:** CVE-2006-6504
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Mozilla Firefox, Mozilla Firefox
- **Affected Products:** 2.0.x, 1.0.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-051/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the browser's handling of SVG comment objects. Firefox does not correctly handle requests to append SVG comments to elements in other types of documents. Attempting such an operation results in a memory corruption that can be exploited to execute arbitrary code.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2006/mfsa2006-73.html

## Disclosure Timeline

- 2006-11-08 - Vulnerability reported to vendor
- 2006-12-19 - Coordinated public release of advisory
