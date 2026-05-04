# ZDI-17-410: Novell ZENworks Reporting Appliance Directory Traversal Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-410
- **ZDI-CAN:** ZDI-CAN-3879
- **Date:** 2017-06-14
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** ZENworks Reporting Appliance
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-410/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on vulnerable installations of Novell ZENworks Reporting Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FCExporter servlet. The process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute arbitrary code under the context of the web server process.

## Additional Details

Micro Focus shipped a fix for this issue in ZENworks reporting v6.2.1 in January 2017.

## Disclosure Timeline

- 2016-07-29 - Vulnerability reported to vendor
- 2017-06-14 - Coordinated public release of advisory
