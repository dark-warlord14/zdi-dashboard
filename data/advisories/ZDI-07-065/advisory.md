# ZDI-07-065: Apple QuickTime Color Table RGB Parsing Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-065
- **ZDI-CAN:** ZDI-CAN-239
- **Date:** 2007-11-05
- **CVE:** CVE-2007-4677
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Ruben Santamarta of reversemode.com and Mario Ballano of 48bits.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-065/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists in the parsing of the CTAB atom. While reading the CTAB RGB values, an invalid color table size can cause QuickTime to write past the end of the heap chunk. This memory corruption can lead to the execution of arbitrary code.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://docs.info.apple.com/article.html?artnum=306896

## Disclosure Timeline

- 2007-09-14 - Vulnerability reported to vendor
- 2007-11-05 - Coordinated public release of advisory
