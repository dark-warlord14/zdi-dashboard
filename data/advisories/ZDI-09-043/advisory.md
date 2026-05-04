# ZDI-09-043: Apple Java CColourUIResource Pointer Dereference Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-043
- **ZDI-CAN:** ZDI-CAN-416
- **Date:** 2009-06-16
- **CVE:** CVE-2009-1719
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Java
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-043/
## Vulnerability Details

his vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Java HotSpot. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the undocumented apple.laf.CColourUIResource(long, int, int ,int, int) constructor. When passing a long integer value as the first argument, the value is interpreted as pointer to an Objective-C object. By constructing a special memory structure and passing the pointer to the first argument an attacker may execute arbitrary code.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3632

## Disclosure Timeline

- 2009-01-26 - Vulnerability reported to vendor
- 2009-06-16 - Coordinated public release of advisory
