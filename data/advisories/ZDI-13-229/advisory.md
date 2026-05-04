# ZDI-13-229: HP PCM+ and Application Lifecycle Management JBoss Invoker Servlets Marshalled Object Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-229
- **ZDI-CAN:** ZDI-CAN-1760
- **Date:** 2013-09-11
- **CVE:** CVE-2013-4810
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard, Hewlett-Packard
- **Affected Products:** Application Lifecycle Management
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-229/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP PCM Plus and Application Lifecycle Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within the exposed EJBInvokerServlet and JMXInvokerServlet. An unauthenticated attacker can post a marshalled object allowing them to install an arbitrary application on the target server. A remote attacker can abuse this to execute remote code under the context of the SYSTEM user in HP PCM Plus and with administrative privileges on Application Lifecycle Management.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03897409 Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03897409

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-09-11 - Coordinated public release of advisory
