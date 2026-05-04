# ZDI-07-078: St. Bernard Open File Manager Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-078
- **ZDI-CAN:** ZDI-CAN-225
- **Date:** 2007-12-17
- **CVE:** CVE-2007-6281
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** St. Bernard
- **Affected Products:** Open File Manager 9.5
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-078/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of St. Bernard Open File Manager. Authentication is not required to exploit this vulnerability. The specific flaw resides in the Open File Manager service, ofmnt.exe, which listens by default on a random TCP port near 1000. The process blindly copies user-suppled data to a static heap buffer. By supplying an overly large amount of data, an attacker can overflow that buffer leading to arbitrary code execution in the context of the SYSTEM user.

## Additional Details

St. Bernard has issued an update to correct this vulnerability. Version 9.6 build 602 available to customers addresses this issue. Other affected vendors such as Hewlett-Packard have made fixes available to customers as well.

## Disclosure Timeline

- 2007-07-20 - Vulnerability reported to vendor
- 2007-12-17 - Coordinated public release of advisory
