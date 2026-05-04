# ZDI-20-678: Trend Micro InterScan Web Security Virtual Appliance Apache Solr Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-678
- **ZDI-CAN:** ZDI-CAN-10329
- **Date:** 2020-05-27
- **CVE:** CVE-2020-8604
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security Virtual Appliance
- **Credit:** Mehmet INCE (@mdisec)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-678/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Trend Micro InterScan Web Security Virtual Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Apache Solr application. When parsing the file parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of IWSS user.

## Additional Details

https://success.trendmicro.com/solution/000253095

## Disclosure Timeline

- 2020-02-04 - Vulnerability reported to vendor
- 2020-05-27 - Coordinated public release of advisory
- 2020-05-28 - Advisory Updated
