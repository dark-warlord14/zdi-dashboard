# ZDI-19-1041: Hewlett Packard Enterprise Intelligent Management Center operatorOnlineList_content Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1041
- **ZDI-CAN:** ZDI-CAN-8965
- **Date:** 2020-01-29
- **CVE:** CVE-2020-24630
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1041/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the operatorOnlineList_content.xhtml or operatorOnlineList_contentOnly.xhtml endpoint. The issue results from displaying sensitive information without authentication as an admin user. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=a00093539en_us

## Disclosure Timeline

- 2019-09-12 - Vulnerability reported to vendor
- 2020-01-29 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
