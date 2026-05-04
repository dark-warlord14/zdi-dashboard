# ZDI-10-028: Skype URI Processing Arbitrary XML File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-028
- **ZDI-CAN:** ZDI-CAN-516
- **Date:** 2010-03-11
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:P
- **Affected Vendors:** Skype
- **Affected Products:** Skype
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-028/
## Vulnerability Details

This vulnerability allows remote attackers to remove arbitrary XML files on vulnerable installations of Skype. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in Skype's handling of the 'skype-plugin:' protocol. An attacker can specify a malicious URI, that upon clicking, will trigger the deletion of an arbitrary attacker specified XML file.

## Additional Details

Nothing.

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2010-03-11 - Coordinated public release of advisory
