# ZDI-08-094: Mozilla Firefox Flash Player Dynamic Module Unloading Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-094
- **ZDI-CAN:** ZDI-CAN-259
- **Date:** 2008-11-12
- **CVE:** CVE-2008-5013
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 2.0.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-094/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on vulnerable installations of Mozilla Firefox with Adobe's Flash Player. User interaction is required in that a user must visit a malicious web site. The specific flaw exists due to a failure to check whether the Flash module has been properly dynamically unloaded. If an SWF file dynamically unloads itself via an outside JavaScript function, the browser will return to an address no longer mapped to the Flash module. Exploitation of this vulnerability can result in arbitrary code execution under the context of the currently logged in user.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2008/mfsa2008-49.html

## Disclosure Timeline

- 2008-05-12 - Vulnerability reported to vendor
- 2008-11-12 - Coordinated public release of advisory
