# ZDI-07-008: Apache Tomcat JK Web Server Connector Long URL Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-008
- **ZDI-CAN:** ZDI-CAN-152
- **Date:** 2007-03-02
- **CVE:** CVE-2007-0774
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apache
- **Affected Products:** Tomcat
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-008/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apache Tomcat JK Web Server Connector. Authentication is not required to exploit this vulnerability. The specific flaw exists in the URI handler for the mod_jk.so library, map_uri_to_worker(), defined in native/common/jk_uri_worker_map.c. When parsing a long URL request, the URI worker map routine performs an unsafe memory copy. This results in a stack overflow condition which can be leveraged to execute arbitrary code.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: http://tomcat.apache.org/connectors-doc/miscellaneous/changelog.html

## Disclosure Timeline

- 2007-02-16 - Vulnerability reported to vendor
- 2007-03-02 - Coordinated public release of advisory
