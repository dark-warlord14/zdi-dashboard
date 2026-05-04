# ZDI-07-068: Apple QuickTime Uncompressedfile Opcode Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-068
- **ZDI-CAN:** ZDI-CAN-242
- **Date:** 2007-11-05
- **CVE:** CVE-2007-4672
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Ruben Santamarta of reversemode.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-068/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must open a malicious image file. The specific flaw exists in the parsing of the pict file format. If an invalid length is specified for the UncompressedQuickTimeData opcode, a stack based buffer overflow occurs, allowing the execution of arbitrary code.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://docs.info.apple.com/article.html?artnum=306896

## Disclosure Timeline

- 2007-09-14 - Vulnerability reported to vendor
- 2007-11-05 - Coordinated public release of advisory
