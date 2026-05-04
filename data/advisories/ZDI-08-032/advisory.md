# ZDI-08-032: Adobe Flash DefineSceneAndFrameLabelData Parsing Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-032
- **ZDI-CAN:** ZDI-CAN-280
- **Date:** 2008-05-22
- **CVE:** CVE-2007-0071
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-032/
## Vulnerability Details

TippingPoint Note: This issue was originally disclosed on April 8, 2008 as ZDI-08-022 but due to an error on our behalf the original advisory was clobbered and is now being re-released as ZDI-08-032. This vulnerability allows attackers to execute arbitrary code on vulnerable installations of the Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the DLL responsible for parsing SWF tags. The vulnerable function trusts an offset present within the vulnerable tag and performs memory operations accordingly. By specifying certain values, an attacker is able to control a memory write leading to arbitrary code execution under the context of the currently logged in user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb08-11.html

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-05-22 - Coordinated public release of advisory
