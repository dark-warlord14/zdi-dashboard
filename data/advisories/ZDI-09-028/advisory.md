# ZDI-09-028: Apple QuickTime CRGN Atom Parsing Heap Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-028
- **ZDI-CAN:** ZDI-CAN-414
- **Date:** 2009-06-02
- **CVE:** CVE-2009-0954
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-028/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of QuickTime Player. User interaction is required to exploit this vulnerability in that the target must either open a malicious file, or visit a malicious web page. The specific flaw exists during parsing of Clipping Region (CRGN) atom types in a Quicktime Movie file. The application trusts the contents of the atom to contain a terminator during a copy operation. The application will copy user-supplied data into a heap-buffer until it identifies this terminator. This will allow one to overwrite heap-control structures which can be leveraged to achieve code execution from the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3591

## Disclosure Timeline

- 2008-12-17 - Vulnerability reported to vendor
- 2009-06-02 - Coordinated public release of advisory
