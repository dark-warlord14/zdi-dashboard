# ZDI-13-063: Hewlett-Packard Intelligent Management Center JavaService Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-063
- **ZDI-CAN:** ZDI-CAN-1663
- **Date:** 2013-04-09
- **CVE:** CVE-2012-5212
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Intelligent Management Center
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-063/
## Vulnerability Details

This vulnerability allows remote attackers to obtain sensitive information on vulnerable installations of HP Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the communication channel between the JavaService server and the Monitoring Deployment Agent. By abusing this flaw an attacker can disclose administrative credentials and possibly leverage this situation to achieve remote code execution. In addition, the application's state can be modified by either stopping all daemons or undeploying the deployed modules.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03689276

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-04-09 - Coordinated public release of advisory
