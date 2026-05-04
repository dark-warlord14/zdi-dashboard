# ZDI-15-581: Hewlett-Packard LoadRunner Virtual Table Server import_database Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-581
- **ZDI-CAN:** ZDI-CAN-3138
- **Date:** 2015-12-02
- **CVE:** CVE-2015-6857
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LoadRunner
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-581/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard LoadRunner. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Virtual Table Server, which listens by default on port 4000. By providing a connection string and malicious SQL commands to the /data/import_database resource, an attacker is able to execute arbitrary SQL commands against the database. An attacker could use this to modify the database, or execute arbitrary code under the context of NETWORK SERVICE.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-c04900820

## Disclosure Timeline

- 2015-09-03 - Vulnerability reported to vendor
- 2015-12-02 - Coordinated public release of advisory
