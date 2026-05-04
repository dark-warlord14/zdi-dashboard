# ZDI-08-047: RealNetworks RealPlayer rmoc3260 ActiveX Control Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-047
- **ZDI-CAN:** ZDI-CAN-270
- **Date:** 2008-07-25
- **CVE:** CVE-2008-1309
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-047/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on vulnerable installations of RealPlayer. User interaction is required in that a user must visit a malicious web site. The specific flaw exists in the rmoc3260 ActiveX control exposed through the following CLSIDs: CFCDAA03-8BE4-11cf-B84B-0020AFBBCCFA 0FDF6D6B-D672-463B-846E-C6FF49109662 224E833B-2CC6-42D9-AE39-90B6A38A4FA2 2F542A2E-EDC9-4BF7-8CB1-87C9919F7F93 3B46067C-FD87-49B6-8DDD-12F0D687035F 3B5E0503-DE28-4BE8-919C-76E0E894A3C2 44CCBCEB-BA7E-4C99-A078-9F683832D493 A1A41E11-91DB-4461-95CD-0C02327FD934 CFCDA953-8BE4-11CF-B84B-0020AFBBCCFA Specifying malicious values for the 'Controls' or 'Console' properties with a specific timing results in a memory corruption which can lead to code execution under the context of the current user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/07252008_player/en/

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-07-25 - Coordinated public release of advisory
