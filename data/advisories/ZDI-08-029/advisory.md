# ZDI-08-029: Trillian AIM.DLL Long HTML Font Parameter Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-029
- **ZDI-CAN:** ZDI-CAN-275
- **Date:** 2008-05-21
- **CVE:** CVE-2008-2407
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Cerulean Studios
- **Affected Products:** Trillian
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-029/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trillian. User interaction is required to exploit this vulnerability in that the target must open a malicious image file. The specific flaws exists during the parsing of messages with overly long attribute values within the FONT tag. The value for any attribute is copied into a stack based buffer via sprintf() which can result in a buffer overrun and can be subsequently leveraged to execute arbitrary code under the privileges of the logged in user. Exploitation may occur over the AIM network or via direct connections.

## Additional Details

Trillian v3.1.10.0 has been released to address these vulnerabilities and is available at http://www.ceruleanstudios.com/downloads/

## Disclosure Timeline

- 2007-12-03 - Vulnerability reported to vendor
- 2008-05-21 - Coordinated public release of advisory
