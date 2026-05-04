# ZDI-17-001: Hewlett Packard Enterprise Operations Orchestration Backwards Compatibility Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-001
- **ZDI-CAN:** ZDI-CAN-3836
- **Date:** 2017-01-10
- **CVE:** CVE-2016-8519
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Operations Orchestration
- **Credit:** Jacob Baines Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-001/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Operations Orchestration. Authentication is not required to exploit this vulnerability. The specific flaw exists within the wsExecutionBridgeService servlet. The issue lies in the failure to properly validate user-supplied data which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-c05361944

## Disclosure Timeline

- 2016-06-30 - Vulnerability reported to vendor
- 2017-01-10 - Coordinated public release of advisory
