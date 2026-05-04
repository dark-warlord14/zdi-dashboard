# ZDI-09-065: Mozilla Firefox TreeColumns Dangling Pointer Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-065
- **ZDI-CAN:** ZDI-CAN-536
- **Date:** 2009-09-10
- **CVE:** CVE-2009-3077
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.0.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-065/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists during the redrawing of tree columns contained within a XUL document. Due to the reuse of a previously freed object, attacker controlled memory can be executed. Successful exploitation of this vulnerability can lead to remote compromise of the affected system under the credentials of the currently logged in user.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2009/mfsa2009-49.html

## Disclosure Timeline

- 2009-07-28 - Vulnerability reported to vendor
- 2009-09-10 - Coordinated public release of advisory
