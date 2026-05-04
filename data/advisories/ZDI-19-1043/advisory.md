# ZDI-19-1043: Hewlett Packard Enterprise Intelligent Management Center addVsiInterfaceInfo Expression Language Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1043
- **ZDI-CAN:** ZDI-CAN-8967
- **Date:** 2020-01-29
- **CVE:** CVE-2020-24652
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1043/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the beanName parameter provided to the addVsiInterfaceInfo.xhtml endpoint. When parsing the beanName parameter, the process does not properly validate a user-supplied string before using it to render a page. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=a00093539en_us

## Disclosure Timeline

- 2019-08-13 - Vulnerability reported to vendor
- 2020-01-29 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
