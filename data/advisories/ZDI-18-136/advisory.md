# ZDI-18-136: Hewlett Packard Enterprise Intelligent Management Center operatorOnlineList_contentOnly Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-136
- **ZDI-CAN:** ZDI-CAN-5093
- **Date:** 2018-01-25
- **CVE:** CVE-2017-8980
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-136/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the operatorOnlineList_contentOnly.jsf endpoint, which listens on TCP ports 8080 and 8443 by default. The issue results from the exposure of session tokens of actively logged-in users. An attacker can leverage this vulnerability to hijack user sessions.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03810en_us

## Disclosure Timeline

- 2017-08-24 - Vulnerability reported to vendor
- 2018-01-25 - Coordinated public release of advisory
- 2018-01-25 - Advisory Updated
