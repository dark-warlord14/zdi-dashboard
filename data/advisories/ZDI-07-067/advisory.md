# ZDI-07-067: Apple QuickTime PICT File Poly Opcodes Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-067
- **ZDI-CAN:** ZDI-CAN-241
- **Date:** 2007-11-05
- **CVE:** CVE-2007-4676
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Ruben Santamarta of reversemode.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-067/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exist in the parsing of Poly type opcodes (opcodes 0x0070-74). Due to improper handling of a malformed element in the structure heap corruption occurs. If properly constructed this can lead to code execution.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://docs.info.apple.com/article.html?artnum=306896

## Disclosure Timeline

- 2007-09-14 - Vulnerability reported to vendor
- 2007-11-05 - Coordinated public release of advisory
