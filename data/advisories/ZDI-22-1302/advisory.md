# ZDI-22-1302: Rockwell Automation ThinManager ThinServer URI Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1302
- **ZDI-CAN:** ZDI-CAN-17482
- **Date:** 2022-09-28
- **CVE:** CVE-2022-38742
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** ThinManager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1302/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Rockwell Automation ThinManager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of HTTPS traffic. When parsing a URI, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the web service.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-270-03

## Disclosure Timeline

- 2022-06-17 - Vulnerability reported to vendor
- 2022-09-28 - Coordinated public release of advisory
