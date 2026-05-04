# ZDI-18-139: Hewlett Packard Enterprise Intelligent Management Center UrlAccessController Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-139
- **ZDI-CAN:** ZDI-CAN-4757
- **Date:** 2018-01-25
- **CVE:** CVE-2017-8982
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-139/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center Smart Connect with Wireless Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UrlAccessController servlet. The issue results from the lack of proper filtering of URLs. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03809en_us

## Disclosure Timeline

- 2017-08-15 - Vulnerability reported to vendor
- 2018-01-25 - Coordinated public release of advisory
- 2018-01-25 - Advisory Updated
