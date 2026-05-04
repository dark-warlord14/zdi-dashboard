# ZDI-08-097: AOL AIM SIPFoundry sipXtapi RTCP Processing Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-097
- **ZDI-CAN:** ZDI-CAN-251
- **Date:** 2008-06-10
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** America Online
- **Affected Products:** AIM
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-097/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AOL AIM. Successful exploitation requires the victim to accept a Video Messaging session with the attacker. The specific flaw exists in the SIP protocol implementation library, sipXtapi.dll. If a malformed RTCP sender report packet is sent, a memory corruption occurs due to a signedness error allowing the execution of arbitrary code.

## Additional Details

Fixed in AIM 6.8 client, version 6.8.7.7.

## Disclosure Timeline

- 2007-12-11 - Vulnerability reported to vendor
- 2008-06-10 - Coordinated public release of advisory
