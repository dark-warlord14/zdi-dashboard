# ZDI-14-387: ARRIS VAP2500 Management Portal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-387
- **ZDI-CAN:** ZDI-CAN-2135
- **Date:** 2014-11-25
- **CVE:** CVE-2014-8425
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** ARRIS
- **Affected Products:** VAP2500
- **Credit:** Ricky "HeadlessZeke" Lawshae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-387/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ARRIS VAP2500. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of access to the management portal. The issue lies in the failure to restrict access to configuration files. An attacker can leverage this vulnerability to leak credentials which can then be chained to execute code with root privileges.

## Additional Details

Vendor has released a hotfix to address the issue: FW08.41

## Disclosure Timeline

- 2014-04-29 - Vulnerability reported to vendor
- 2014-11-25 - Coordinated public release of advisory
