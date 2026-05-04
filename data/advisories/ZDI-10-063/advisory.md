# ZDI-10-063: Mozilla Firefox Cross Document DOM Node Moving Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-063
- **ZDI-CAN:** ZDI-CAN-761
- **Date:** 2010-04-05
- **CVE:** CVE-2010-1121
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** Nils of MWR InfoSecurity (http://twitter.com/MWRlabs)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-063/
## Vulnerability Details

This vulnerability allows remote attackers to bypass specific script execution enforcements on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists when moving DOM nodes in between documents with a specific timing while triggering garbage collection. If timed correctly Firefox will incorrectly reference a previously freed object which can be leveraged by an attacker to execute arbitrary code under the context of the current user.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-25.html

## Disclosure Timeline

- 2010-03-26 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
