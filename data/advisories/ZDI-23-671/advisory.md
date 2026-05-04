# ZDI-23-671: Delta Industrial Automation DIALink Directory Traversal Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-671
- **ZDI-CAN:** ZDI-CAN-16888
- **Date:** 2023-05-17
- **CVE:** CVE-2022-2969
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** DIALink
- **Credit:** Y4er
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-671/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Delta Industrial Automation DIALink. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the opcua endpoint of the web service, which listens on TCP port 5000 by default. When parsing the filename parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create files in the context of the web service.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-22-307-03

## Disclosure Timeline

- 2022-07-26 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
