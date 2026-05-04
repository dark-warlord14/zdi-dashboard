# ZDI-11-143: Cisco Unified CallManager xmldirectorylist.jsp SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-143
- **ZDI-CAN:** ZDI-CAN-965
- **Date:** 2011-04-28
- **CVE:** CVE-2011-1610
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** Cisco Call Manager
- **Credit:** Sven Taute
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-143/
## Vulnerability Details

This vulnerability allows remote attackers to inject arbitrary SQL into the backend database on vulnerable installations of Cisco Unified CM. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Call Manager component. The system exposes an Apache webserver which contains a JSP script vulnerable to SQL injection. The xmldirectorylist.jsp file does not properly validate the f, l, and n parameters before passing them to the database. A remote attacker can abuse this to inject SQL statements to be evaluated by the underlying database.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://www.cisco.com/warp/public/707/cisco-sa-20110427-cucm.shtml

## Disclosure Timeline

- 2010-11-05 - Vulnerability reported to vendor
- 2011-04-28 - Coordinated public release of advisory
