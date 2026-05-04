# ZDI-10-272: RealNetworks RealPlayer Cook Audio Codec Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-272
- **ZDI-CAN:** ZDI-CAN-506
- **Date:** 2010-12-10
- **CVE:** CVE-2010-4377
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-272/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious media file. The specific flaw exists in the parsing of audio codec information encapsulated in a Real Audio media file. While processing cook audio codec data the number of subbands is improperly calculated. By specifying a large number of subbands an allocated heap chunk can be overflown. Successful exploitation can result in system compromise under the credentials of the currently logged in user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/12102010_player/en/

## Disclosure Timeline

- 2009-06-25 - Vulnerability reported to vendor
- 2010-12-10 - Coordinated public release of advisory
