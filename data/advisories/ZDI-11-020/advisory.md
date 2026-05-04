# ZDI-11-020: Oracle Beehive voice-servlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-020
- **ZDI-CAN:** ZDI-CAN-814
- **Date:** 2011-01-18
- **CVE:** CVE-2010-4417
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Beehive
- **Credit:** 1c239c43f521145fa8385d64a9c32243 of unsecurityresearch.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-020/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Beehive. Authentication is not required to exploit this vulnerability. The specific flaw exists within 'voice-servlet/prompt-qa/Index.jspf'. During the creation of a file used for storing an evaluation parameter user supplied data is used to create a filename and another user specified field is later used to populate that file's contents. By inserting a null byte (0x00) into the filename the user can control the extension of the newly created file. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the oracle user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2011-194091.html

## Disclosure Timeline

- 2010-06-09 - Vulnerability reported to vendor
- 2011-01-18 - Coordinated public release of advisory
