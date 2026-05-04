# ZDI-13-262: HP Application Lifecycle Management GossipService SOAP Request Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-262
- **ZDI-CAN:** ZDI-CAN-1759
- **Date:** 2013-11-24
- **CVE:** CVE-2013-4836
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Application Lifecycle Management
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-262/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Application Lifecycle Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service named GossipServiceSoapBinding. This web service is vulnerable to SQL injection. A remote attacker can leverage this to gain remote code execution under the context of the postgres user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03969436

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
