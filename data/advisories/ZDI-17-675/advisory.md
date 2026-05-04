# ZDI-17-675: Hewlett Packard Enterprise Intelligent Management Center dnd Expression Language Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-675
- **ZDI-CAN:** ZDI-CAN-4853
- **Date:** 2017-08-11
- **CVE:** CVE-2017-12511
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-675/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the actionInput form field in the dnd.jsf endpoint. When parsing the actionInput parameter, the process does not properly validate a user-supplied string before using it to render a page. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03768en_us

## Disclosure Timeline

- 2017-06-05 - Vulnerability reported to vendor
- 2017-08-11 - Coordinated public release of advisory
