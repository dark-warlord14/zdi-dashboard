# ZDI-08-098: AOL AIM SIPFoundry sipXtapi RTP Processing Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-098
- **ZDI-CAN:** ZDI-CAN-279
- **Date:** 2008-06-10
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** America Online
- **Affected Products:** AIM
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-098/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of any communication application utilizing the SIP Foundry API. This includes vendors such as AOL, Yahoo, Skype, Oracle, Nortel and more. Authentication is not required to exploit these vulnerabilities, however a user must have a voice session active to expose the flaw. The specific flaw exists when parsing RTP information destined for the target client. When the value for the RTP header value "Extension Length" is improperly used a heap overflow occurs. Proper exploitation can lead to remote compromise of the system under the credentials of the logged in user.

## Additional Details

Fixed in AIM 6.8 client, version 6.8.7.7.

## Disclosure Timeline

- 2008-01-21 - Vulnerability reported to vendor
- 2008-06-10 - Coordinated public release of advisory
